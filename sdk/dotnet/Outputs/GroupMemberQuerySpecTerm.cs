// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln.Outputs
{

    [OutputType]
    public sealed class GroupMemberQuerySpecTerm
    {
        public readonly string? Op;
        public readonly string? Property;
        public readonly string? Tag;
        public readonly string? Value;

        [OutputConstructor]
        private GroupMemberQuerySpecTerm(
            string? op,

            string? property,

            string? tag,

            string? value)
        {
            Op = op;
            Property = property;
            Tag = tag;
            Value = value;
        }
    }
}