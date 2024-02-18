// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cpln

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/pulumiverse/pulumi-cpln/sdk/go/cpln/internal"
)

type OrgLogging struct {
	pulumi.CustomResourceState

	CoralogixLoggings OrgLoggingCoralogixLoggingArrayOutput `pulumi:"coralogixLoggings"`
	CplnId            pulumi.StringOutput                   `pulumi:"cplnId"`
	DatadogLoggings   OrgLoggingDatadogLoggingArrayOutput   `pulumi:"datadogLoggings"`
	Description       pulumi.StringOutput                   `pulumi:"description"`
	ElasticLoggings   OrgLoggingElasticLoggingArrayOutput   `pulumi:"elasticLoggings"`
	LogzioLoggings    OrgLoggingLogzioLoggingArrayOutput    `pulumi:"logzioLoggings"`
	Name              pulumi.StringOutput                   `pulumi:"name"`
	S3Loggings        OrgLoggingS3LoggingArrayOutput        `pulumi:"s3Loggings"`
	Tags              pulumi.StringMapOutput                `pulumi:"tags"`
}

// NewOrgLogging registers a new resource with the given unique name, arguments, and options.
func NewOrgLogging(ctx *pulumi.Context,
	name string, args *OrgLoggingArgs, opts ...pulumi.ResourceOption) (*OrgLogging, error) {
	if args == nil {
		args = &OrgLoggingArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OrgLogging
	err := ctx.RegisterResource("cpln:index/orgLogging:OrgLogging", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrgLogging gets an existing OrgLogging resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrgLogging(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrgLoggingState, opts ...pulumi.ResourceOption) (*OrgLogging, error) {
	var resource OrgLogging
	err := ctx.ReadResource("cpln:index/orgLogging:OrgLogging", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OrgLogging resources.
type orgLoggingState struct {
	CoralogixLoggings []OrgLoggingCoralogixLogging `pulumi:"coralogixLoggings"`
	CplnId            *string                      `pulumi:"cplnId"`
	DatadogLoggings   []OrgLoggingDatadogLogging   `pulumi:"datadogLoggings"`
	Description       *string                      `pulumi:"description"`
	ElasticLoggings   []OrgLoggingElasticLogging   `pulumi:"elasticLoggings"`
	LogzioLoggings    []OrgLoggingLogzioLogging    `pulumi:"logzioLoggings"`
	Name              *string                      `pulumi:"name"`
	S3Loggings        []OrgLoggingS3Logging        `pulumi:"s3Loggings"`
	Tags              map[string]string            `pulumi:"tags"`
}

type OrgLoggingState struct {
	CoralogixLoggings OrgLoggingCoralogixLoggingArrayInput
	CplnId            pulumi.StringPtrInput
	DatadogLoggings   OrgLoggingDatadogLoggingArrayInput
	Description       pulumi.StringPtrInput
	ElasticLoggings   OrgLoggingElasticLoggingArrayInput
	LogzioLoggings    OrgLoggingLogzioLoggingArrayInput
	Name              pulumi.StringPtrInput
	S3Loggings        OrgLoggingS3LoggingArrayInput
	Tags              pulumi.StringMapInput
}

func (OrgLoggingState) ElementType() reflect.Type {
	return reflect.TypeOf((*orgLoggingState)(nil)).Elem()
}

type orgLoggingArgs struct {
	CoralogixLoggings []OrgLoggingCoralogixLogging `pulumi:"coralogixLoggings"`
	DatadogLoggings   []OrgLoggingDatadogLogging   `pulumi:"datadogLoggings"`
	ElasticLoggings   []OrgLoggingElasticLogging   `pulumi:"elasticLoggings"`
	LogzioLoggings    []OrgLoggingLogzioLogging    `pulumi:"logzioLoggings"`
	S3Loggings        []OrgLoggingS3Logging        `pulumi:"s3Loggings"`
}

// The set of arguments for constructing a OrgLogging resource.
type OrgLoggingArgs struct {
	CoralogixLoggings OrgLoggingCoralogixLoggingArrayInput
	DatadogLoggings   OrgLoggingDatadogLoggingArrayInput
	ElasticLoggings   OrgLoggingElasticLoggingArrayInput
	LogzioLoggings    OrgLoggingLogzioLoggingArrayInput
	S3Loggings        OrgLoggingS3LoggingArrayInput
}

func (OrgLoggingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*orgLoggingArgs)(nil)).Elem()
}

type OrgLoggingInput interface {
	pulumi.Input

	ToOrgLoggingOutput() OrgLoggingOutput
	ToOrgLoggingOutputWithContext(ctx context.Context) OrgLoggingOutput
}

func (*OrgLogging) ElementType() reflect.Type {
	return reflect.TypeOf((**OrgLogging)(nil)).Elem()
}

func (i *OrgLogging) ToOrgLoggingOutput() OrgLoggingOutput {
	return i.ToOrgLoggingOutputWithContext(context.Background())
}

func (i *OrgLogging) ToOrgLoggingOutputWithContext(ctx context.Context) OrgLoggingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrgLoggingOutput)
}

func (i *OrgLogging) ToOutput(ctx context.Context) pulumix.Output[*OrgLogging] {
	return pulumix.Output[*OrgLogging]{
		OutputState: i.ToOrgLoggingOutputWithContext(ctx).OutputState,
	}
}

// OrgLoggingArrayInput is an input type that accepts OrgLoggingArray and OrgLoggingArrayOutput values.
// You can construct a concrete instance of `OrgLoggingArrayInput` via:
//
//	OrgLoggingArray{ OrgLoggingArgs{...} }
type OrgLoggingArrayInput interface {
	pulumi.Input

	ToOrgLoggingArrayOutput() OrgLoggingArrayOutput
	ToOrgLoggingArrayOutputWithContext(context.Context) OrgLoggingArrayOutput
}

type OrgLoggingArray []OrgLoggingInput

func (OrgLoggingArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrgLogging)(nil)).Elem()
}

func (i OrgLoggingArray) ToOrgLoggingArrayOutput() OrgLoggingArrayOutput {
	return i.ToOrgLoggingArrayOutputWithContext(context.Background())
}

func (i OrgLoggingArray) ToOrgLoggingArrayOutputWithContext(ctx context.Context) OrgLoggingArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrgLoggingArrayOutput)
}

func (i OrgLoggingArray) ToOutput(ctx context.Context) pulumix.Output[[]*OrgLogging] {
	return pulumix.Output[[]*OrgLogging]{
		OutputState: i.ToOrgLoggingArrayOutputWithContext(ctx).OutputState,
	}
}

// OrgLoggingMapInput is an input type that accepts OrgLoggingMap and OrgLoggingMapOutput values.
// You can construct a concrete instance of `OrgLoggingMapInput` via:
//
//	OrgLoggingMap{ "key": OrgLoggingArgs{...} }
type OrgLoggingMapInput interface {
	pulumi.Input

	ToOrgLoggingMapOutput() OrgLoggingMapOutput
	ToOrgLoggingMapOutputWithContext(context.Context) OrgLoggingMapOutput
}

type OrgLoggingMap map[string]OrgLoggingInput

func (OrgLoggingMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrgLogging)(nil)).Elem()
}

func (i OrgLoggingMap) ToOrgLoggingMapOutput() OrgLoggingMapOutput {
	return i.ToOrgLoggingMapOutputWithContext(context.Background())
}

func (i OrgLoggingMap) ToOrgLoggingMapOutputWithContext(ctx context.Context) OrgLoggingMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrgLoggingMapOutput)
}

func (i OrgLoggingMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*OrgLogging] {
	return pulumix.Output[map[string]*OrgLogging]{
		OutputState: i.ToOrgLoggingMapOutputWithContext(ctx).OutputState,
	}
}

type OrgLoggingOutput struct{ *pulumi.OutputState }

func (OrgLoggingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OrgLogging)(nil)).Elem()
}

func (o OrgLoggingOutput) ToOrgLoggingOutput() OrgLoggingOutput {
	return o
}

func (o OrgLoggingOutput) ToOrgLoggingOutputWithContext(ctx context.Context) OrgLoggingOutput {
	return o
}

func (o OrgLoggingOutput) ToOutput(ctx context.Context) pulumix.Output[*OrgLogging] {
	return pulumix.Output[*OrgLogging]{
		OutputState: o.OutputState,
	}
}

func (o OrgLoggingOutput) CoralogixLoggings() OrgLoggingCoralogixLoggingArrayOutput {
	return o.ApplyT(func(v *OrgLogging) OrgLoggingCoralogixLoggingArrayOutput { return v.CoralogixLoggings }).(OrgLoggingCoralogixLoggingArrayOutput)
}

func (o OrgLoggingOutput) CplnId() pulumi.StringOutput {
	return o.ApplyT(func(v *OrgLogging) pulumi.StringOutput { return v.CplnId }).(pulumi.StringOutput)
}

func (o OrgLoggingOutput) DatadogLoggings() OrgLoggingDatadogLoggingArrayOutput {
	return o.ApplyT(func(v *OrgLogging) OrgLoggingDatadogLoggingArrayOutput { return v.DatadogLoggings }).(OrgLoggingDatadogLoggingArrayOutput)
}

func (o OrgLoggingOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *OrgLogging) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

func (o OrgLoggingOutput) ElasticLoggings() OrgLoggingElasticLoggingArrayOutput {
	return o.ApplyT(func(v *OrgLogging) OrgLoggingElasticLoggingArrayOutput { return v.ElasticLoggings }).(OrgLoggingElasticLoggingArrayOutput)
}

func (o OrgLoggingOutput) LogzioLoggings() OrgLoggingLogzioLoggingArrayOutput {
	return o.ApplyT(func(v *OrgLogging) OrgLoggingLogzioLoggingArrayOutput { return v.LogzioLoggings }).(OrgLoggingLogzioLoggingArrayOutput)
}

func (o OrgLoggingOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *OrgLogging) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o OrgLoggingOutput) S3Loggings() OrgLoggingS3LoggingArrayOutput {
	return o.ApplyT(func(v *OrgLogging) OrgLoggingS3LoggingArrayOutput { return v.S3Loggings }).(OrgLoggingS3LoggingArrayOutput)
}

func (o OrgLoggingOutput) Tags() pulumi.StringMapOutput {
	return o.ApplyT(func(v *OrgLogging) pulumi.StringMapOutput { return v.Tags }).(pulumi.StringMapOutput)
}

type OrgLoggingArrayOutput struct{ *pulumi.OutputState }

func (OrgLoggingArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OrgLogging)(nil)).Elem()
}

func (o OrgLoggingArrayOutput) ToOrgLoggingArrayOutput() OrgLoggingArrayOutput {
	return o
}

func (o OrgLoggingArrayOutput) ToOrgLoggingArrayOutputWithContext(ctx context.Context) OrgLoggingArrayOutput {
	return o
}

func (o OrgLoggingArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*OrgLogging] {
	return pulumix.Output[[]*OrgLogging]{
		OutputState: o.OutputState,
	}
}

func (o OrgLoggingArrayOutput) Index(i pulumi.IntInput) OrgLoggingOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OrgLogging {
		return vs[0].([]*OrgLogging)[vs[1].(int)]
	}).(OrgLoggingOutput)
}

type OrgLoggingMapOutput struct{ *pulumi.OutputState }

func (OrgLoggingMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OrgLogging)(nil)).Elem()
}

func (o OrgLoggingMapOutput) ToOrgLoggingMapOutput() OrgLoggingMapOutput {
	return o
}

func (o OrgLoggingMapOutput) ToOrgLoggingMapOutputWithContext(ctx context.Context) OrgLoggingMapOutput {
	return o
}

func (o OrgLoggingMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*OrgLogging] {
	return pulumix.Output[map[string]*OrgLogging]{
		OutputState: o.OutputState,
	}
}

func (o OrgLoggingMapOutput) MapIndex(k pulumi.StringInput) OrgLoggingOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OrgLogging {
		return vs[0].(map[string]*OrgLogging)[vs[1].(string)]
	}).(OrgLoggingOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OrgLoggingInput)(nil)).Elem(), &OrgLogging{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrgLoggingArrayInput)(nil)).Elem(), OrgLoggingArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OrgLoggingMapInput)(nil)).Elem(), OrgLoggingMap{})
	pulumi.RegisterOutputType(OrgLoggingOutput{})
	pulumi.RegisterOutputType(OrgLoggingArrayOutput{})
	pulumi.RegisterOutputType(OrgLoggingMapOutput{})
}