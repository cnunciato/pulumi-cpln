// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln.Inputs
{

    public sealed class SecretAzureConnectorArgs : global::Pulumi.ResourceArgs
    {
        [Input("code", required: true)]
        private Input<string>? _code;
        public Input<string>? Code
        {
            get => _code;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _code = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("url", required: true)]
        private Input<string>? _url;
        public Input<string>? Url
        {
            get => _url;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _url = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public SecretAzureConnectorArgs()
        {
        }
        public static new SecretAzureConnectorArgs Empty => new SecretAzureConnectorArgs();
    }
}
